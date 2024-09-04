class triangle:
    def P_T_2(self, row_index:int)->list[int]:
        result=[[1]]

        for i in range(row_index):
            temp=[0]+result[-1]+[0]
            new_row=[]

            for j in range(len(result[-1])+1):
                new_row.append(temp[j]+temp[j+1])
            result.append(new_row)

        return result[-1]
    
value=triangle()

print(value.P_T_2(3))
