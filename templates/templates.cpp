#include<iostream>
#include<string>
using namespace std;

#include "value.h"
#include "word.h"

class NewBadClass {
    public:
    NewBadClass & operator + (const NewBadClass & other)
    {
        return *this;
    }
};

template<class a, class b>
b calculate(a x, b y)
{
    return b(x * y);
}


template<typename t>
class PT
{};

template<typename t>
class CT : public PT<t>
{};

int main()
{
    CT<string> the_ct;
    Words<int> words_with_ints;
    words_with_ints.AddThing(7);
    words_with_ints.AddThing(3);
    words_with_ints.AddThing(4);
    words_with_ints.PrintThings();

    Value<int> int_values;
    Value<double> d_values;
    Value<long> long_vals;
    Value<string> string_vals;
    Value<NewBadClass> bad_vals;
    cout << int_values.Add(3, 6) << " " << d_values.Add(4.2, 7.9) << endl;
    cout << string_vals.Add("first thing", "robot");
    NewBadClass x, y;
    bad_vals.Add(x, y);
    int ix = 5;
    double dy = 3.7;
    cout << endl << calculate(dy, ix) << endl;

    cout << endl << calculate(ix, dy) << endl;
    
    return 0;
}