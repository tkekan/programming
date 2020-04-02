#include<iostream>

using namespace std;

class I {
  public:
    virtual ~I(){}
    virtual void do_it() = 0;
};

class A: public I {
  public:
    A () {
        cout << "Calling A ctor\n";
    }
    ~A() {
        cout << "A dtor" << '\n';
    }
    /*virtual*/
    void do_it() {
        cout << "Calling A do_it\n";
        cout << 'A';
    }
};

class D: public I {
  public:
    D(I *inner) {
        cout << "Calling D ctor: ";
        m_wrappee = inner;
        cout << typeid(inner).name() << endl;
    }
    ~D() {
        delete m_wrappee;
    }
    /*virtual*/
    void do_it() {
        cout << "Calling D do_it\n";
        m_wrappee->do_it();
    }
  private:
    I *m_wrappee;
};

class X: public D {
  public:
    X(I *core): D(core){
        cout << "Calling X ctor\n";
    }
    ~X() {
        cout << "X dtor" << "   ";
    }
    /*virtual*/
    void do_it() {
        cout << "Calling X do_it\n";
        D::do_it();
        cout << 'X';
    }
};

class Y: public D {
  public:
    Y(I *core): D(core){
        cout << "Calling Y ctor\n";
    }
    ~Y() {
        cout << "Y dtor" << "   ";
    }
    /*virtual*/
    void do_it() {
        cout << "Calling Y do_it\n";
        D::do_it();
        cout << 'Y';
    }
};

class Z: public D {
  public:
    Z(I *core): D(core){}
    ~Z() {
        cout << "Z dtor" << "   ";
    }
    /*virtual*/
    void do_it() {
        D::do_it();
        cout << 'Z';
    }
};

int main() { 
 // I *anX = new X(new A);
  I *anXY = new Y(new X(new A));
  //I *anXYZ = new Z(new Y(new X(new A)));
  //anX->do_it();
 // cout << '\n';
  anXY->do_it();
 // cout << '\n';
 // anXYZ->do_it();
 // cout << '\n';
 // delete anX;
 // delete anXY;
 // delete anXYZ;
  return 0;
}
