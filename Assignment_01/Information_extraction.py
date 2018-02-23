from __future__ import print_function
import re
import spacy

from pyclausie import ClausIE


nlp = spacy.load('en')
re_spaces = re.compile(r'\s+')


class Person(object):
    def __init__(self, name, likes=None, has=None, travels=None):
        """
        :param name: the person's name
        :type name: basestring
        :param likes: (Optional) an initial list of likes
        :type likes: list
        :param dislikes: (Optional) an initial list of likes
        :type dislikes: list
        :param has: (Optional) an initial list of things the person has
        :type has: list
        :param travels: (Optional) an initial list of the person's travels
        :type travels: list
        """
        self.name = name
        self.likes = [] if likes is None else likes
        self.has = [] if has is None else has
        self.travels = [] if travels is None else travels

    def __repr__(self):
        return self.name


class Pet(object):
    def __init__(self, pet_type, s, name=None):
        self.name = name
        self.type = pet_type
        self.occupier = s

class Trip(object):
    def __init__(self, date, place,traveller):
        self.departs_on = date
        self.departs_to = place
        self.traveller = traveller


persons = []
pets = []
trips = []
root = None

def get_data_from_file(file_path='./assignment_01.data'):
    with open(file_path) as infile:
        cleaned_lines = [line.strip() for line in infile if not line.startswith(('$$$', '###', '==='))]

    return cleaned_lines


def select_person(name):
    for person in persons:
        if person.name == name:
            return person


def add_person(name):
    person = select_person(name)

    if person is None:
        new_person = Person(name)
        persons.append(new_person)

        return new_person

    return person


def select_pet(name):
    for pet in pets:
        if pet.name == name:
            return pet


def add_pet(type, s, name=None):
    pet = None

    if name:
        pet = select_pet(name)

    if pet is None:
        pet = Pet(type,s, name)
        pets.append(pet)

    return pet


def get_persons_pet(person_name):

    person = select_person(person_name)

    for thing in person.has:
        if isinstance(thing, Pet):
            return thing

def select_place(time, name):
    for place in trips:
        if place.traveller == name and place.departs_on==time:
            return place


def add_place(time, name, to=None):
    place = None

    if name:
        place = select_place(time, name)

    if place is None:
        place = Trip(time, to, name)
        trips.append(place)

    return place

def get_persons_travel(person_name):

    person = select_person(person_name)

    for thing in person.travels:
        if isinstance(thing, Trip):
            return thing

def get_persons_trip(time, person_name):

    trip = select_place(time, person_name)

    return trip

    #for thing in person.travels:
        #if isinstance(thing, Trip):
            #return thing

def process_relation_triplet(triplet):
    """
    Process a relation triplet found by ClausIE and store the data

    find relations of types:
    (PERSON, likes, PERSON)
    (PERSON, has, PET)
    (PET, has_name, NAME)
    (PERSON, travels, TRIP)
    (TRIP, departs_on, DATE)
    (TRIP, departs_to, PLACE)

    :param triplet: The relation triplet from ClausIE
    :type triplet: tuple
    :return: a triplet in the formats specified above
    :rtype: tuple
    """

    sentence = triplet.subject + ' ' + triplet.predicate + ' ' + triplet.object

    doc = nlp(unicode(sentence))
    global root
    for t in doc:
        if t.pos_ == 'VERB' and t.head == t:
            root = t
        # elif t.pos_ == 'NOUN'

    # also, if only one sentence
    # root = doc[:].root


    """
    CURRENT ASSUMPTIONS:
    - People's names are unique (i.e. there only exists one person with a certain name).
    - Pet's names are unique
    - The only pets are dogs and cats
    - Only one person can own a specific pet
    - A person can own only one pet
    """


    # Process (PERSON, likes, PERSON) relations
    if root.lemma_ == 'like' and 'does' not in triplet.predicate :
        if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON' or (e.label_=='ORG')] and triplet.object in [e.text for e in doc.ents if e.label_ == 'PERSON']:
            s = add_person(triplet.subject)
            o = add_person(triplet.object)
            s.likes.append(o)

    if root.lemma_ == 'be' and triplet.object.startswith('friends with'):
        fw_doc1 = nlp(unicode(triplet.object))
        #with_token = [t for t in fw_doc if t.text == 'with'][0]
        #fw_who = [t for t in with_token.children if t.dep_ == 'pobj'][0].text
        # fw_who = [e for e in fw_doc.ents if e.label_ == 'PERSON'][0].text

        if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON']:
            s = add_person(triplet.subject)
            for e in fw_doc1.ents:
                if e.label_ == 'PERSON':
                    fw_who1 = e.text
                    o = add_person(fw_who1)
                    s.likes.append(o)
                    o.likes.append(s)


    if len([e.text for e in doc.ents if e.label_ == 'PERSON'])==2 and triplet.object == 'friends':
        # Sally and Mary are friends.
        doc_new = nlp(unicode(triplet.subject))
        likename = [e.text for e in doc_new.ents if e.label_=='PERSON']
        sname = likename[0]
        oname = likename[1]
        s = add_person(sname)
        o = add_person(oname)
        s.likes.append(o)
        o.likes.append(s)

        return 'likes'


    # Process (PET, has, NAME)
    if triplet.subject.endswith('name') and ('dog' in triplet.subject or 'cat' in triplet.subject):
        obj_span = doc.char_span(sentence.find(triplet.object), len(sentence))

        # handle single names, but what about compound names? Noun chunks might help.
        if len(obj_span) >= 1 and obj_span[0].pos_ == 'PROPN':
            name = triplet.object
            doc2=nlp(unicode(triplet.object))
            chunks = list(doc2.noun_chunks)
            name = chunks[0].text
            subj_start = sentence.find(triplet.subject)
            subj_doc = doc.char_span(subj_start, subj_start + len(triplet.subject))

            s_people = [token.text for token in subj_doc if token.ent_type_ == 'PERSON']
            assert len(s_people) == 1
            s_person = select_person(s_people[0])

            s_pet_type = 'dog' if 'dog' in triplet.subject else 'cat'

            pet = add_pet(s_pet_type, s_people, name)

            s_person.has.append(pet)

    if root.lemma_ == 'have' and ('dog' in triplet.object or 'cat' in triplet.object):
        if 'named' in triplet.object:
            if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON']:
                a = add_person(triplet.subject)
                name_pos = triplet.object.find('named')
                pet_name = triplet.object[name_pos + 6:]
                if a.has:
                    if a.has[0].name:
                        a = 0
                    else:
                        a.has[0].name = pet_name
                else:
                    x_pet_type = 'dog' if 'dog' in triplet.object else 'cat'
                    pet = add_pet(x_pet_type, a,  pet_name)
                    a.has.append(pet)


    # Process(Person, departs_to, place)
    if [e.text for e in doc.ents if e.label_ == 'GPE']:
        personname = [e.text for e in doc.ents if e.label_ == 'PERSON' or e.label_=='ORG']
        date = [str(e.text) for e in doc.ents if e.label_ == 'DATE']
        place = [str(e.text) for e in doc.ents if e.label_ == 'GPE']
        for person in personname:
            s= add_person(person)
            o= add_place(date, s.name, place)
            s.travels.append(o)


def preprocess_question(question):
    # remove articles: a, an, the

    q_words = question.split(' ')

    # when won't this work?
    for article in ('a', 'an', 'the'):
        try:
            q_words.remove(article)
        except:
            pass

    return re.sub(re_spaces, ' ', ' '.join(q_words))


def has_question_word(string):
    # note: there are other question words
    for qword in ('who', 'what'):
        if qword in string.lower():
            return True

    return False



def main():
    sents = get_data_from_file()

    cl = ClausIE.get_instance()

    triples = cl.extract_triples(sents)

    for t in triples:
        r = process_relation_triplet(t)
        #print(r)

    question = ' '
    while question[-1] != '?':
        question = raw_input("Please enter your question: ")

        if question[-1] != '?':
            print('This is not a question... please try again')

    q_trip = cl.extract_triples([preprocess_question(question)])[0]


    # (Who, likes, PERSONS)
    if q_trip.subject.lower() == 'who' and q_trip.predicate=='likes':
        answer = '{} likes {}'
        qdoc = nlp(unicode(question))
        personname = [str(e.text) for e in qdoc.ents if e.label_=='PERSON' or (e.label_=="ORG")][0]
        for person in persons:
            personlike = set(person.likes)
            for a in personlike:
                if personname == a.name:
                    print (person.name)

    # (Who, does, person, like)
    if q_trip.object.lower() == 'who' and q_trip.predicate=='does like':
        answer = '{} likes {}'
        qdoc = nlp(unicode(question))
        personname = [e.text for e in qdoc.ents if e.label_=='PERSON'][0]
        x=select_person(personname)
        for person in x.likes:
            personlike = set(x.likes)
            print (person.name)

    # (WHO, has, PET)
    # here's one just for dogs
    if q_trip.subject.lower() == 'who' and ('dog' in q_trip.object or 'cat' in q_trip.object):
        answer = '{} has a {} named {}.'
        pet_type = 'dog' if 'dog' in q_trip.object else 'cat'
        for person in persons:
            pet = get_persons_pet(person.name)
            if pet:
                if pet.type == pet_type:
                    print(person.name)

    #(Does, person, like, person)
    if 'does' in q_trip.subject.lower() and q_trip.predicate == 'like':
        qdoc = nlp(unicode(question))
        personname = [(e.text) for e in qdoc.ents if e.label_=='PERSON']
        for person in persons:
            if person.name == personname[0]:
                for person1 in person.likes:
                    if person1.name == personname[1]:
                       print('YES')
                    else:
                       print('NO')

    #(Who, travels, where)
    if q_trip.subject.lower() == 'who' and q_trip.predicate == 'is flying' or q_trip.predicate == 'is going' or q_trip.predicate == 'is traveling':
        answer = '{} is flying to {}.'
        qdoc = nlp(unicode(question))
        personname = [str(e.text) for e in qdoc.ents if e.label_ == 'PERSON' or (e.label_ == "ORG")]
        personplace = [str(e.text) for e in qdoc.ents if e.label_ == 'GPE']
        for person in persons:
            for trip in person.travels:
                if trip and trip.departs_to == personplace:
                    print (person.name)

    #(When, person, travels, where)
    if 'when' in q_trip.object.lower():
        answer = '{} is flying to {} on {}'
        qdoc = nlp(unicode(question))
        personname = [str(e.text) for e in qdoc.ents if e.label_ == 'PERSON' or (e.label_ == "ORG")]
        personplace = [str(e.text) for e in qdoc.ents if e.label_ == 'GPE']
        # date = [str(e.text) for e in qdoc.ents if e.label_ == 'DATE']
        p = select_person(personname[0])
        x=1
        for trip in p.travels:
                if trip.departs_to == personplace:
                    print(trip.departs_on)
                    x=0
        if x:
            print("Sorry we don;t know")

    #(What's the name of <person>'s <pet_type>)
    if question.startswith('what'):
        qdoc = nlp(unicode(question))
        persono= [str(e.text) for e in qdoc.ents if e.label_ == 'PERSON' or (e.label_ == "ORG")]
        p = add_person(persono[0])
        pet_type = 'dog' if 'dog'in question else 'cat'
        for x in p.has:
            if x.type == pet_type:
                print (x.name)
    else:
        IE= ClausIE.get_instance()
        q_trip = IE.extract_triples([preprocess_question(question)])[0]
if __name__ == '__main__':
    main()
