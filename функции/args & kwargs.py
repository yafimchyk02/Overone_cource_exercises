def many (*args,**kwargs):
    print(args)
    print(kwargs)

many(1,2,3,4,5,6,5, name = 'Mike', job = 'Programmer')