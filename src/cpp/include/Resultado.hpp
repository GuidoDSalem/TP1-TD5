#ifndef RESULTADO
#define RESULTADO

#include<vector>

class Resultado{

    public:
    
        float bestError;
        double time;
        std::vector<float> solutionX;
        std::vector<float> solutionY;

        Resultado();

};


#endif//RESULTADO