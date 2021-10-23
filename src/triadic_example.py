from fcatools.triadic import triadic_io, triadic_flat
from src.fcatools.dyadic import dyadic_concepts, dyadic_lattice, dyadic_generators, dyadic_rules
from src.fcatools.triadic import triadic_rules


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

    concepts = dyadic_concepts.read_concepts_from_file(output_file='data_examples/pnrks_dyadic_concepts.txt')
    print(concepts)

    lattice = dyadic_lattice.build_lattice_iPred(concepts)
    print(lattice)

    generators = dyadic_generators.compute_generators(lattice)
    print(generators)

    dyadic_association_rules = dyadic_rules.compute_association_rules(lattice, generators)
    print(dyadic_association_rules)

    bacars_implication_rules, bacars_association_rules = \
        triadic_rules.calculate_bacars_from_dyadic_rules(dyadic_association_rules, '-')

    bcaars_implication_rules, bcaars_association_rules = \
        triadic_rules.calculate_bcaars_from_dyadic_rules(dyadic_association_rules, '-')

    print(bacars_implication_rules)
    print(bacars_association_rules)

    print(bcaars_implication_rules)
    print(bcaars_association_rules)


if __name__ == '__main__':
    main()
