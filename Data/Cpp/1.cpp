#include <iostream>
#include <string>

using namespace std;

class CString
{
private:
    string str;
    int coords;

public:
    CString(string s = "", int c = 0)
    {
        str = s;
        coords = c;
    }
    void print()
    {
        for (int i = 0; i < coords; i++)
            cout << "\t";
        cout << str << endl;
    }
    friend void ch_coords(CString x, int nc)
    {
        x.coords = nc;
    }
};

int main()
{
    string s;
    int c;
    CString x[30];
    for (int i = 0; i < 30; i++)
    {
        cin >> s;

        x[i] = CString(s, i % 3);
    }
    ch_coords(x[29], 2);
    for (int i = 0; i < 30; i++)
        x[i].print();
    return 0;
}
