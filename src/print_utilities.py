import os
from src.utilities import diagram_as_graph

def cppArrayPrint(lst):
    return str(lst).replace('[','{').replace(']','}')


def create_diagram_gpu_file(laphDiagrams, allBaryonTensors, allBaryonTensorsBack, allBaryonSinks, allBaryonProps):
    s=cpp_file_header()
    for d in laphDiagrams:
        for blocks,contraction in diagram_as_graph(d,allBaryonTensors).items():
            blocks=blocks.split(',')


            block0=allBaryonTensorsBack[int(blocks[0])]
            block1=allBaryonTensorsBack[int(blocks[1])]
            
            if block0[0:3]=="B^*":
                b0type='bprops'
                b0Idx=allBaryonProps[block0]
            else: 
                b0type='bsinks'
                b0Idx=allBaryonSinks[block0]
            
            if block1[0:3]=="B^*":
                b1type='bprops'
                b1Idx=allBaryonProps[block1]
            else:
                b1type='bsinks'
                b1Idx=allBaryonSinks[block1]

            s+="  diagrams.push_back(Diagram({}[{}],{}[{}],std::vector<std::vector<int>>{}));\n".format(b0type,b0Idx,b1type,b1Idx,cppArrayPrint(contraction))

    s+=cpp_file_footer()

    fileName = os.path.join("Output","define_diagrams_gpu.cpp")
    file=open(fileName,"w")
    file.write(s)
    file.close()


def cpp_file_header():
    s = ""
    s += "#include \"define_diagrams.h\"\n"
    s += "#include \"diagram_utils.h\"\n"
    s += "#include <complex>\n"
    s += "#include <iostream>\n\n"

    s += "using namespace std;\n"
    s += "using Tensor4 = Eigen::Tensor<std::complex<double>,4>;\n"
    s += "using cd = std::complex<double>;  \n\n"

    s += "struct Diagram { \n"
    s += "  const Tensor4 &bLeft, &bRight; \n"
    s += "  std::vector<std::vector<int>> contractions; \n"
    s += "  Diagram(const Tensor4 &left, const Tensor4 &right, std::vector<std::vector<int>> contracts):bLeft(left),bRight(right),contractions(contracts){}\n"
    s += "};\n\n"


    s += "void compute_diagrams(vector<cd> &res, const vector<Tensor4> &bprops, const vector<Tensor4> &bsinks) \n"
    s += "{\n"
    s += "  std::vector<Diagram> diagrams;\n"

    return s


def cpp_file_footer():
    s = ""

    s += "  for(size_t i=0; i<diagrams.size(); ++i)\n"
    s += "  {\n"
    s += "    const Diagram d = diagrams[i]; \n"
    s += "    res[i]=cuTensor_contract(d.bLeft,d.bRight,d.contractions);\n"
    s += "  }\n"

    s += "}  \n"

    return s