#include <iostream>


using namespace std;


class Calc{
	private:
		int width;
		int height;
		int **a;
	
	public:
		Calc(int m, int n, int **mass){
			width = m;
			height = n;
			a = new int*[m];
			for (int i=0; i < m; i++) a[i] = new int[n];
			
			for (int i=0; i < m; i++){
				for (int j=0; n > j; j++){
					a[i][j] = mass[i][j];
				}
			}
		}
		
		void printf(){
			for (int i=0; i < width; i++){
				for (int j=0; height > j; j++){
					cout<<a[i][j]<<"\t";
				}
				cout<<endl;
			}
		}
		
		bool operator <<(int k){
			bool f=false;
			for (int i=0; i < width; i++){
				for (int j=0; height > j; j++){
					if(a[i][j] == k) f=true;
				}
			}
			return f;
		}
		
		Calc operator -(Calc l){
			int **b = new int*[this->width];
			for (int i=0; i < this->width; i++) b[i] = new int[this->height];
			for (int i=0; i < this->width; i++){
				for (int j=0; this->height > j; j++){
					b[i][j] = this->a[i][j];
				}
			}
			for (int i=0; i < width; i++){
				for (int j=0; height > j; j++){
					b[i][j] -= l.a[i][j];
				}
			}
			
			return Calc(this->width, this->height, b);
		}
		
		Calc operator=(Calc l){
			a = l.a;
			width = l.width;
			height = l.height;
			return *this;
		}
};


int main(){
	int **x1;
	x1 = new int*[2];
	for (int i=0; i<2; i++){
		x1[i] = new int[2];
		for (int j=0; j<2; j++){
			cin>>x1[i][j];
		}
	}
	int **x2;
	x2 = new int*[2];
	for (int i=0; i<2; i++){
		x2[i] = new int[2];
		for (int j=0; j<2; j++){
			cin>>x2[i][j];
		}
	}
	Calc m1 = Calc(2, 2, x1);
	Calc m2 = Calc(2, 2, x2);
	bool f = m1<<2;
	cout<<"===="<<endl;
	cout<< f <<endl;
	cout<<"===="<<endl;
	Calc m3 = m1-m2;
	cout<<"===="<<endl;
	m3.printf();
	
	return 0;
}

