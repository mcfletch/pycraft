template = '''else if (parameters.size() == %(argsize)s) {
    return (Object) this.pointer.invoke
        (cls.cast(message.instance) %(argcoerces)s
    );
}'''
argcoerce = '''parameters.get(%(argindex)s)'''


for i in range(0, 10):
    params = dict(argsize=i)
    argcoerces = []
    for argindex in range(0, i):
        argcoerces.append(
            argcoerce
            % {
                'argindex': argindex,
            }
        )
    params['argcoerces'] = '' if not argcoerces else (', ' + ", ".join(argcoerces))
    print(template % params)
