def get_distances_between_wp(descriptor_vector, metric_function):
    final_summ = [[] for _ in descriptor_vector]
    for i in range(len(descriptor_vector)):
        for j in range(i + 1, len(descriptor_vector)):
            cos = metric_function(descriptor_vector[i], descriptor_vector[j])
            final_summ[i].append(cos)
            final_summ[j].append(cos)
    return final_summ