def floodFill2(image, sr, sc, starting_color, target_color):
        if (sr > len(image) - 1) or sr < 0:
            return image
        if (sc > len(image[0]) - 1) or sc < 0:
            return image
        if image[sr][sc] != starting_color:
            return image
        if image[sr][sc] == target_color:
            return image
        
        image[sr][sc] = target_color
        
        top = (sr-1, sc)
        bottom = (sr+1, sc)
        left = (sr, sc-1)
        right = (sr, sc+1)
        
        floodFill2(image, top[0], top[1], starting_color, target_color)
        floodFill2(image, bottom[0], bottom[1], starting_color, target_color)
        floodFill2(image, left[0], left[1], starting_color, target_color) 
        floodFill2(image, right[0], right[1], starting_color, target_color)   
        
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
print(floodFill2(image, sr, sc, image[sr][sc], 2))