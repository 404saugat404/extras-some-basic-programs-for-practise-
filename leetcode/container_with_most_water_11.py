def water(height:list[int]):
    l=0
    r=len(height)-1
    max_area=float("-inf")

    while l<r:
        area=min(height[l],height[r])*(r-l)

        max_area=max(area,max_area)

        if height[l]<height[r]:
            l=l+1

        else:
            r=r-1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(water(height=height))