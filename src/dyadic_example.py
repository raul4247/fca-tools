from fcatools.dyadic import dyadic_io


def main():

    dyadic_context = dyadic_io.read_dyadic_context_data(path='data_examples/pnrks_dyadic.data')

    objects = dyadic_context.objects
    attributes = dyadic_context.attributes
    incidences = dyadic_context.incidences
    # density = dyadic_context.density

    print(objects)
    print(attributes)
    print(incidences)

    # cex = dyadic_io.read_dyadic_context_cex(path='pnrks_dyadyc.cex')

    dyadic_io.write_dyadic_context_data(dyadic_context, path='my.csv')


if __name__ == '__main__':
    main()
