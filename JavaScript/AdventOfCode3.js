const fs = require("fs") 

function input(name, delim = "\n") {
	return fs.readFileSync(`Js/${name}.in`, {encoding: "latin1"}).split(delim)
}
map=input(3)
function AdventOfCode31()
{
    x=0
    y=0
    trees=0
    while(y<map.length)
    {
        line=map[y]
        if(x>line.length-2)
        {
            x=x-(line.length-1)
        }
        if(line[x]=='#')
        {
            trees++
        }
        x+=3
        y++
    }
    return trees
}
function AdventOfCode32()
{

    dirx=1
    diry=1
    TreesMultiplied=1
    for(;;)
    {
        x=0
        y=0
        trees=0
        while(y<map.length)
        {
            line=map[y]
            if(x>line.length-2)
            {
                x=x-(line.length-1)
            }
            if(line[x]=='#')
            {
                trees++
            }
            x+=dirx
            y+=diry
        }
        console.log(trees)
        TreesMultiplied*=trees
        dirx+=2
        if(dirx>7)
        {
            dirx=1
            diry+=1
        }
        if(diry>1 & dirx>1)
        {
            return TreesMultiplied
        }
    }
}
console.log(AdventOfCode31(), AdventOfCode32())