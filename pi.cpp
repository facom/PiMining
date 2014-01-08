/*
################################################################################
#  ___ _     __  __ _      _           
# | _ (_)___|  \/  (_)_ _ (_)_ _  __ _ 
# |  _/ |___| |\/| | | ' \| | ' \/ _` |
# |_| |_|   |_|  |_|_|_||_|_|_||_\__, |
#                                |___/ 
################################################################################
# 2014 (C) Jorge I. Zuluaga zuluagajorge@gmail.com
################################################################################
# Pi has been downloaded from:
# http://micronetsoftware.com/pi_day
################################################################################
# LINEAR SEARCH
################################################################################
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

#define K 1E4
#define M 1E6
#define G 1E9

typedef long long Long;
typedef char Int;
unsigned SI;
FILE *FPI;

Long piSegment(Long offset,Int length)
{
  Long segment;
  int i;
  Int* n=(Int*)calloc(length,sizeof(Int));
  fseek(FPI,offset*SI,SEEK_SET);
  fread(n,sizeof(Int),length,FPI);
  Long fac=1;
  segment=0;
  for(i=length-1;i>=0;i--){
    segment+=n[i]*fac;
    fac*=10;
  }
  return segment;
}

int main(int argc,char *argv[])
{
  Int n,ndigits;
  Long i,number,segment;
  Long maxdigits;

  SI=sizeof(Int);
  FPI=fopen("numbers/pi.bin","rb");

  if(argc<=1){
    fprintf(stderr,"You should provide an integer string to search.\n");
    exit(1);
  }
  number=atoll(argv[1]);
  ndigits=(Int)strlen(argv[1]);
  if(argv[2]!=NULL){
    maxdigits=(Long)atof(argv[2]);
  }else maxdigits=100*K;
  

  fprintf(stdout,"Looking for number: %lld\n",number);
  fprintf(stdout,"Number of digits: %d\n",ndigits);
  fprintf(stdout,"Searching section: %lld first digits\n",maxdigits);

  for(i=0;i<maxdigits;i++){
    segment=piSegment(i,ndigits);
    if(segment==number){
      fprintf(stdout,"%lld ",i);
      fflush(stdout);
    }
  }
  fprintf(stdout,"\n");
  return 0;
}
