#include "define_diagrams.h"
#include "diagram_utils.h"
#include <complex>
#include <iostream>

using namespace std;
using Tensor4 = Eigen::Tensor<std::complex<double>,4>;
using cd = std::complex<double>;  

struct Diagram { 
  const Tensor4 &bLeft, &bRight; 
  std::vector<std::vector<int>> contractions; 
  Diagram(const Tensor4 &left, const Tensor4 &right, std::vector<std::vector<int>> contracts):bLeft(left),bRight(right),contractions(contracts){}
};

void compute_diagrams(vector<cd> &res, const vector<Tensor4> &bprops, const vector<Tensor4> &bsinks) 
{
  std::vector<Diagram> diagrams;
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 3}, {2, 2}, {1, 1}, {0, 0}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 3}, {2, 2}, {1, 0}, {0, 1}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 0}, {2, 2}, {1, 3}, {0, 1}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 1}, {2, 2}, {1, 3}, {0, 0}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 1}, {2, 2}, {1, 0}, {0, 3}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 0}, {2, 2}, {1, 1}, {0, 3}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 3}, {2, 2}, {1, 1}, {0, 0}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 3}, {2, 0}, {1, 1}, {0, 2}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 1}, {2, 2}, {1, 3}, {0, 0}}));
  diagrams.push_back(Diagram(bprops[0],bsinks[0],std::vector<std::vector<int>>{{3, 1}, {2, 0}, {1, 3}, {0, 2}}));
  for(size_t i=0; i<diagrams.size(); ++i)
  {
    const Diagram d = diagrams[i]; 
    res[i]=cuTensor_contract(d.bLeft,d.bRight,d.contractions);
  }
}  
