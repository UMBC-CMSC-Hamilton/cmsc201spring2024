template<typename t>
class Value
{
    public:
        Value() {}
        t GetFirst() const {return m_var1;}
        t GetSecond() const {return m_var2;}
        void SetFirst(t new_first) {m_var1 = new_first;}
        void SetSecond(t new_second) {m_var2 = new_second;}
        t Add(t v1, t v2)
        {
            return v1 + v2;
        }
    private:
        t m_var1;
        t m_var2;
};