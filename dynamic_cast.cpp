#include <iostream>
using namespace std;

class Base
{
public:
    virtual void DoIt() { cout << endl << "Base"; };    // pure virtual
    virtual ~Base() {};
    void BaseIt() { cout << endl << "Basing it";}
};

class Foo : public Base
{
public:
    virtual void DoIt() { cout << endl << "Foo"; }
    void FooIt() { cout << "Fooing It..."; }
};

class Bar : public Base
{
int count;
public :
    void setcount(int val) { count = val; }
    virtual void DoIt() { cout << "Bar"; }
    void BarIt() { cout << endl << "baring It..."; }
};


int main()
{

        Base *base = new Bar;
        Foo *foo = dynamic_cast<Foo *>(base);
        if (foo)
            foo->DoIt();
        else
            cout << "NULL";
        /*
        Bar* bar = new Bar;
        printf("Bar : %p sizeof %lu",bar,sizeof(*bar));
        bar->setcount(10);
        bar->BarIt();
        Base* base = dynamic_cast<Base*>(bar);
        base->BaseIt();
        printf("\nBase address is %p",base);
        printf("\nsizeof %lu",sizeof(*base));
        //bar->setcount(10); */
  return 0;
}
