screen tinymap:
  frame:
    xsize 400
    ysize 400
    viewport:
        scrollbars "both"
        draggable True
        child_size (500,500)
        for i in range(50):
            for j in range(20):
                if i%3==0:
                    add "blue tile.png" xpos (i+j)*17 ypos (i-j)*8
                elif i%3==1:
                    add "green tile.png" xpos (i+j)*17 ypos (i-j)*8
                else:
                    add "red tile.png" xpos (i+j)*17 ypos (i-j)*8
