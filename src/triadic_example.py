from fcatools.triadic.triadic_context import TriadicContext
from fcatools.triadic.triadic_association_rule import TriadicAssociationRule as tar

from fcatools.dyadic.dyadic_concept import DyadicConcept
from fcatools.dyadic.dyadic_lattice import DyadicLattice



def main():
    triadic_context = TriadicContext.read_triadic_context_data(path='data_examples/pnrks_triadic.data')

    objects = triadic_context.objects
    attributes = triadic_context.attributes
    conditions = triadic_context.conditions
    incidences = triadic_context.incidences

    print(objects)
    print(attributes)
    print(conditions)
    for value in incidences:
        print(value)

    dyadic_context = triadic_context.flat_triadic_to_dyadic()
    for value in dyadic_context.incidences:
        print(value)
    print(dyadic_context.objects)
    print(dyadic_context.attributes)
    # triadic_io.write_triadic_context_csv(triadic_context, "triadic.data")

    concepts = DyadicConcept.read_concepts_from_file(output_file='data_examples/pnrks_dyadic_concepts.txt')
    print("\n\nconcepts:")
    for value in concepts:
        print(value)

    lattice, _ = DyadicLattice.build_lattice_iPred(concepts)
    print("lattice:")
    print(lattice)

    generators = lattice.compute_generators()
    print('\ngenerators:')
    for value in generators:
        print(value)

    dyadic_association_rules = lattice.compute_association_rules(generators)
    print('\nDyadic Association Rules:')
    for value in dyadic_association_rules:
        print(value)

    bacars_implication_rules, bacars_association_rules = \
        tar.calculate_bacars_from_dyadic_rules(dyadic_association_rules, '-')

    bcaars_implication_rules, bcaars_association_rules = \
        tar.calculate_bcaars_from_dyadic_rules(dyadic_association_rules, '-')

    print('\nBACARS Rules:')
    print('implications:')
    for value in bacars_implication_rules:
        print(value)
    print('associations:')
    for value in bacars_association_rules:
        print(value)

    print('\nBCAARS Rules:')
    print('implications:')
    for value in bcaars_implication_rules:
        print(value)
    print('associations:')
    for value in bcaars_association_rules:
        print(value)


if __name__ == '__main__':
    main()
