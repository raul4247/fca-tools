from fcatools.dyadic import dyadic_io, dyadic_concept, dyadic_lattice


def main():
    dyadic_context = dyadic_io.read_dyadic_context_data(path='data_examples/pnrks_dyadic.data')

    objects = dyadic_context.objects
    attributes = dyadic_context.attributes
    incidences = dyadic_context.incidences
    # density = dyadic_context.density

    print(objects)
    print(attributes)
    print(incidences)

    # concepts = dyadic_concept.get_concepts_d_peeler(
    #     context_file='data_examples/pnrks_dyadic.data',
    #     output_file='pnrks_concepts.txt'
    # )

    concepts = dyadic_concept.read_concepts_from_file(output_file='pnrks_concepts.txt')
    print(concepts)

    lattice = dyadic_lattice.build_lattice_iPred(concepts)

    print(lattice)


if __name__ == '__main__':
    main()
