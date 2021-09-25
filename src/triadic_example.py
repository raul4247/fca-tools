from fcatools.triadic import triadic_io, triadic_flat
from src.fcatools.dyadic import dyadic_concept, dyadic_lattice


def main():

    triadic_context = triadic_io.read_triadic_context_data(path='data_examples/pnrks_triadic.data')

    objects = triadic_context.objects
    attributes = triadic_context.attributes
    conditions = triadic_context.conditions
    incidences = triadic_context.incidences

    print(objects)
    print(attributes)
    print(conditions)
    print(incidences)

    dyadic_context = triadic_flat.flat_triadic_to_dyadic(triadic_context)
    print(dyadic_context.incidences)
    print(dyadic_context.objects)
    print(dyadic_context.attributes)
    # triadic_io.write_triadic_context_csv(triadic_context, "triadic.data")

    concepts = dyadic_concept.read_concepts_from_file(output_file='pnrks_concepts.txt')
    print(concepts)

    lattice = dyadic_lattice.build_lattice_iPred(concepts)
    print(lattice)

if __name__ == '__main__':
    main()
