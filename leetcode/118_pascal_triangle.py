class triangle:
    def pascal_triangle(self,numRows:int)->int:
        result=[[1]]

        for i in range(numRows-1):
            temp=[0]+result[-1]+[0]
            new_row=[]
            for j in range(len(result[-1])+1):
                new_row.append(temp[j]+temp[j+1])
            result.append(new_row)

        return result 


value=triangle()

print(value.pascal_triangle(5))