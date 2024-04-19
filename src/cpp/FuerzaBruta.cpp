#include "include/FuerzaBruta.hpp"

float fuerzaBrutaRecursiva(
    vector<float> &gridX,
    vector<float> &gridY,
    vector<float> &xs,
    vector<float> &ys,
    vector<float> &res,
    float bestError_,
    int k,
    const json &datos)
{

    //CASOS BASE

    if( k == 0 ){
        if(xs[0] != gridX[0]){
            return 100000001;
        }
        if(xs[xs.size()-1] != gridX[gridX.size()-1]){
            return 100000001;
        }

        for(int i=0; i< xs.size()-2;i++){
            if(xs[i] > xs[i+1] ){
                return 100000001;
            }
        }

        float error = errorBreakPoint(xs,ys,datos);

        if(error < bestError_){
            /*std::cout<<"ERROR: "<<error;
            printVector(&ys, " - BEST YS: ");
            */
            res = ys;
            res.clear();
            for(int i=0;i < ys.size();i++){
                res.push_back(ys[i]);
            }
            
            


            return error;
        }
        return bestError_;
    }


    //PASO RECURSIVO
    float bestError = bestError_;
    float error;

    for(int i=0; i<gridX.size();i++){
        xs.push_back(gridX[i]);
        for(int j=0; j< gridY.size();j++){
            //TODO
            ys.push_back(gridY[j]);
            error = fuerzaBrutaRecursiva(gridX,gridY,xs,ys,res,bestError,k-1,datos);

            if(error < bestError){
                bestError = error;
            }
            
            ys.pop_back();

        }
        xs.pop_back();
    }

    return bestError;

}

void fuerzaBruta(Resultado &res, int m, int n,int k, const json &data){
    auto inicio = high_resolution_clock::now();

    std::vector<float> grillaX;
    std:vector<float> grillaY;

    linspace(grillaX,minJson(data,"x"),maxJson(data,"x"),m);
    linspace(grillaY, minJson(data, "y"), maxJson(data, "y"), n);

    vector<float> xs;
    vector<float> ys;
    vector<float> result;

    float bestError = fuerzaBrutaRecursiva(grillaX,grillaY,xs,ys,result,10000001,k,data);

    // res.bestError = bestError;
    
    auto fin = high_resolution_clock::now();
    double duracion = (double)duration_cast<duration<double>>(fin - inicio).count();
    

    std::cout << "BEST_ERROR: " << bestError << "  TIME: " << duracion << endl;
    res.time = duracion;
    res.bestError = bestError;

    printVector(&result);
}
