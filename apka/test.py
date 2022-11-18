class baza:

    def dodawanie(self):
        return  1 + 1

class pod(baza):

    def dodawanie(self):
        return super(pod, self).dodawanie()

a = pod()
print(a.dodawanie())