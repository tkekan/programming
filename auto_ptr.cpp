#include <iostream>
#include <memory>

using namespace std;

class Double
{
public:
    Double(double d = 0) : dValue(d) { cout << "constructor: " << dValue << endl; } 
    ~Double() { cout << "destructor: " << dValue << endl; }
    void setDouble(double d) { dValue = d; }
private:
    double dValue;
}; 


Double allocate()
{
    cout << "Inside Allocate" << endl;
    auto_ptr<Double> ptr(new Double(3.14));
    (*ptr).setDouble(6.28); 
    cout << "exiting Allocate" << endl;
    return *ptr;
}

int main()
{   
    Double ptr =  allocate();
    //auto_ptr<Double> ptr(new Double(3.14));
    ptr.setDouble(10.28);
    Double *ptr1 = new Double();
    ptr1->setDouble(20.28);
    return 0;
}
