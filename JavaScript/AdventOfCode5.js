const fs = require("fs") 

function input(name, delim = "\n") {
	return fs.readFileSync(`Js/${name}.in`, {encoding: "latin1"}).split(delim)
}

function FB(seat)
{
    Start=0
    end=127
    i=0
    while(i<seat.length-3)
    {
        if(seat[i]=='B')
        {
            Start=Math.ceil((end+Start)/2)
        }
        else if(seat[i]=='F')
        {
            end=Math.floor((end+Start)/2)
        }
        i++
    }
    return end
}

function LR(seat)
{
    Start=0
    end=7
    k=seat.length-3
    while(k<seat.length)
    {
        if(seat[k-1]=='R')
        {
            Start=Math.ceil((end+Start)/2)
        }
        else if(seat[k-1]=='L')
        {
            end=Math.floor((end+Start)/2)
        }
        k++

    }
    return end
}

seats=input(5)

function AdventOfCode51()
{
    j=0
    HighestID=0
    while(j<seats.length)
    {
        seatID=((FB(seats[j])*8)+LR(seats[j]))
        if(seatID>HighestID)
        {
            HighestID=seatID
        }
        j++
    }
    return HighestID
}

function AdventOfCode52()
{
    j=0
    MyID=0
    num=0
    var free=new Set()
    while(j<seats.length)
    {
        seatID=((FB(seats[j])*8)+LR(seats[j]))
        free.add(seatID)
        j++
    }
    for(let item of free)
    {
        if(free.has(item+1)!=true & free.has(item-1)==true & free.has(item+2)==true)
        {
            return MyID=item+1
        }
        num++
    }
}

console.log(AdventOfCode51(), AdventOfCode52())