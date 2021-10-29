# from fcatools.dyadic import dyadic_io, dyadic_concepts, dyadic_lattice
# from src.fcatools.dyadic import dyadic_generators, dyadic_rules
# from src.fcatools.triadic import triadic_rules

from fcatools.dyadic.dyadic_context import DyadicContext
from fcatools.dyadic.dyadic_concept import DyadicConcept
from fcatools.dyadic.dyadic_lattice import DyadicLattice

def main():

    dyadic_context = DyadicContext.read_dyadic_context_data(path='data_examples/pnrks_dyadic.data')

    print(f'Objects count: {len(dyadic_context.objects)}')
    print(f'Attributes count: {len(dyadic_context.attributes)}')

    density = dyadic_context.get_density() * 100
    print(f'Context density: {"{:.2f}".format(density)}%')

    # Requires d-peeler !!!
    # concepts = dyadic_concepts.get_concepts_d_peeler(
    #     context_file='data_examples/pnrks_dyadic.data',
    #     output_file='data_examples/pnrks_dyadic_concepts.txt'
    # )

    concepts = DyadicConcept.read_concepts_from_file(output_file='data_examples/pnrks_dyadic_concepts.txt')
    print(f'Concepts count: {len(concepts)}')

    lattice, links = DyadicLattice.build_lattice_iPred(concepts)
    print(f'Lattice created {len(links)} links between concepts')

    generators = lattice.compute_generators()
    print(f'Generators count: {len(generators)}')
    for generator in generators:
        print(generator)

    rules = lattice.compute_association_rules(generators)
    print(f'Rules count: {len(rules)}')
    for rule in rules:
        print(rule)

    # impl_bacars, assoc_bacars = triadic_rules.calculate_bacars_from_dyadic_rules(rules, '-')
    # print(f'BACARS (implication) count: {len(impl_bacars)}')
    # print(f'BACARS (association) count: {len(assoc_bacars)}')

    # print(impl_bacars)
    # print(assoc_bacars)

    # impl_bcaars, assoc_bcaars = triadic_rules.calculate_bcaars_from_dyadic_rules(rules, '-')
    # print(f'BCAARS (implication) count: {len(impl_bcaars)}')
    # print(f'BCAARS (association) count: {len(assoc_bcaars)}')

    # print(impl_bcaars)
    # print(assoc_bcaars)


if __name__ == '__main__':
    main()
