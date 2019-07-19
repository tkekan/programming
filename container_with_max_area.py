int maxArea(int A[], int len) 
{ 
    int l = 0; 
    int r = len -1; 
    int area = 0; 
      
    while (l < r) 
    { 
        // Calculating the max area 
        area = max(area, min(A[l], 
                        A[r]) * (r - l)); 
                          
            if (A[l] < A[r]) 
                l += 1; 
                  
            else
                r -= 1; 
    } 
    return area; 
} 
