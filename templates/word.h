/**
 * Moral of this horrible story:
 * Everything goes into the .h file [no .cpp]
 * Only compile the other files, where you include this template class
*/
#ifndef __WORD_H__
#define __WORD_H__

#include <vector>
#include <string>
#include <iostream>
using namespace std;

template<class the_type>
class Words
{
    public:
        void AddWord(string new_string);
        void AddThing(the_type thing);
        void PrintThings();
        void PrintWords();
    private:
        vector<the_type> m_things;
        vector<string> m_words;
};

#include "word.cpp"
#endif 