def get_types_of_event_spacy(name, nlp_with_type_ent) -> list:
    return list(map(str, nlp_with_type_ent(name).ents))