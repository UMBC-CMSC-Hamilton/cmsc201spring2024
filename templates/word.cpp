#ifndef __WORD_CPP__
#define __WORD_CPP__
#include "word.h"
#include <iostream>

/**
 * Do not compile this file ALONE
 * 
*/
template<class the_type>
void Words<the_type>::AddWord(string new_string)
{
    m_words.push_back(new_string);
}

template<class the_type>
void Words<the_type>::AddThing(the_type thing)
{
    m_things.push_back(thing);
}
template<class the_type>
void Words<the_type>::PrintThings()
{
    for(unsigned i = 0; i < m_things.size();i++)
        cout << m_things[i] << " ";
    // adding a requirement that m_things[i] is cout-able
    cout << endl;
}
template<class the_type>
void Words<the_type>::PrintWords()
{
    for(unsigned i = 0; i < m_words.size();i++)
        cout << m_words[i] << " ";
    cout << endl;
}
#endif 
