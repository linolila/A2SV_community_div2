class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    #    return [[x ^ 1 for x in reversed(img)] for img in image]
       for img in image :
            img.reverse()
            for i in range(len(image)) :
                img[i]^=1
       return image
         
