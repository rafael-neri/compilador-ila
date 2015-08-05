//============================================================================
// Name        : compilador-ila-c-cpp.cpp
// Author      : Equipe Tatu
// Version     : 0.1
// Copyright   : Todos os direitos reservados.
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
using std::cout;
using std::cin;
using std::endl;

class LexAnaliser {
private:
        FILE *file;
        string token;
        unsigned char* data;
        unsigned long fileSize;
public:
       FILE* getFile() {
               return file;
       };
       string getToken() {
              return token;
       };
       unsigned char* getData() {
                return data;
       };
       unsigned long getFileSize() {
                return fileSize;
       };
       void setFile(FILE *f) {
            this->file = f;
       };
       void setToken(string t) {
            this->token = t;
       };
       void setData(unsigned char* d) {
            this->data = d;
       };
       void setFileSize(unsigned long f) {
            this->fileSize = f;
       };
};

long getFileInfo(FILE* inputFile, long offset, int numberOfChars) {
     unsigned char			*ptrC;
     long				value = 0L;
     unsigned char			dummy;
     int				i;
     dummy = '0';
     ptrC = &dummy;

     fseek(inputFile, offset, SEEK_SET);

     for(i=1; i<=numberOfChars; i++) {
              fread(ptrC, sizeof(char), 1, inputFile);
              /* calculate value based on adding bytes */
              value = (long)(value + (*ptrC)*(pow(256, (i-1))));
     }
     return(value);
}

//int main(int argc, char *argv[]) {
int main() {
    LexAnaliser    lex;
    lex.setFile(fopen("src/teste.txt","r")); /* Arquivo ASCII, para leitura */
//    fseek(lex.getFile(), 0L, SEEK_END);
//    lex.setFileSize(getFileInfo(lex.getFile(), 2, 4));
//    unsigned char* u = (unsigned char)* malloc(lex.getFileSize()*sizeof(unsigned char));
//    lex.setData(u);
//    cout << "Archive:" << endl;
    //FILE* s = lex.getFile();

    if(!lex.getFile())
    {
           cout << "Erro na abertura do arquivo" <<endl;
           exit(0);
    }
    char c;
    while((c = getc(lex.getFile())) != EOF) {      /* Enquanto não chegar ao final do arquivo */
             cout << " " ;
             cout << c;                            /* imprime o caracter lido */
    }
    fclose(lex.getFile());
    cout << "[" << lex.getData();
    cout << "] " << endl;

    cout << "Tamanho do arquivo: " << lex.getFileSize() << " Bytes" << endl;
    //system("PAUSE");
    return 1;
}
