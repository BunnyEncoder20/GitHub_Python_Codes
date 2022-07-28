#include<stdio.h>
#include<string.h>

char ipclass(char ip_address[])
{
    char str[4];
    int i=0;
    while (ip_address[i]!='.')
    {
        str[i]=ip_address[i];
        i++;
    }
    i--; int ip=0,j=1;
    while (i>=0)
    {
        ip+=(ip_address[i]-'0')*j;     
        j*=10; i--;
    }   //converting the string into a interger value for comparision

    //printf("ip_address in interger : %d\n",ip);
    if (ip>=1 && ip<=127) //first octet range for A class
        return 'A';
    else if (ip>=128 && ip<=191) //first octet range for B class
        return 'B';
    else if (ip >= 192 && ip <= 223) //first octet range for c class
        return 'C';
    else if (ip >= 224 && ip <= 239)//first octet range for D class
        return 'D';
    else
        return 'E';
}

void network_host_id(char ip_address[], char ip_class)
{
    char network_id[15],host_id[15];
    for (int i = 0; i < 15; i++)
    {
        network_id[i]='\0';
        host_id[i]='\0';
    }   //initilization with null to prevent junk values from displaying
    int i=0,j=0,counter=0;  
    //using counter to differenciate subnet mask of different classes

    if (ip_class=='A')  //subnet class A = 8
    {
       while (ip_address[j]!='.')   
       {
           network_id[i]=ip_address[j];
           i++; j++;
       }
       i=0;j++; 
       while (ip_address[j]!='\0')
       {
           host_id[i]=ip_address[j];
           i++;j++;
       }
       
       printf("Network_Id is : %s\nHost_Id is : %s",network_id,host_id);
    }

    else if (ip_class=='B') //subnet class B = 16
    {
       while (counter<2)   
       {
           network_id[i]=ip_address[j];
           if(ip_address[j]=='.')
                counter++; 
           i++; j++; 
       }
       i=0;
       while (ip_address[j]!='\0')
       {
           host_id[i]=ip_address[j];
           i++;j++;
       }
       
       printf("Network_Id is : %s\nHost_Id is : %s",network_id,host_id); 
    }

    else if (ip_class=='C')  //subnet class C = 24
    {
        while (counter<3)   
       {
           network_id[i]=ip_address[j];
           if(ip_address[j]=='.')
                counter++; 
           i++; j++; 
       }
       i=0; 
       while (ip_address[j]!='\0')
       {
           host_id[i]=ip_address[j];
           i++;j++;
       }
       
       printf("Network_Id is : %s\nHost_Id is : %s",network_id,host_id);
    }
    
    else //IP address of class D & E cannot be seperated into network and host IDs
    {
        printf("IP Address of %c class cannot be seperated into Network and Host ID.\n",ip_class);
    }
}

int main()
{
    char ip_address[30];
    scanf("%[^\n]%*c", ip_address); //to take input of string untill newline character
    char ip_class = ipclass(ip_address);
    printf("Class : %c\n",ip_class);
    network_host_id(ip_address,ip_class);
    return 0;
}
