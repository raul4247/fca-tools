from fcatools.triadic import triadic_io, triadic_flat


def main():

    triadic_context = triadic_io.read_triadic_context_data(path='pnrks_triadic.data')

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


if __name__ == '__main__':
    main()
