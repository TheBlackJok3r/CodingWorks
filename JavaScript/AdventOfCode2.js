const fs = require("fs") 

function input(name, delim = "\n") {
	return fs.readFileSync(`Js/${name}.in`, {encoding: "latin1"}).split(delim)
}

function letters(letter, word)
{
    ret=0
    i=0
    while(i<word.length)
    {
        if(word[i]==letter)
        {
            ret++
        }
        i++
    }
    return ret
}

function ToDash(chain)
{
    i=0
    k=0
    ret=0
    while(i<chain.length)
    {
        if(chain[i]=='-')
            break
        else
        {
            if(k==0)
            {
                ret=chain[i]
            }
            else
            {
                ret=ret+chain[i]
            }
            k+=1
        }
        i++
    }
    return ret
}


function AfterDash(chain)
{
    i=chain.length-1
    k=0
    ret=0
    while(i>0)
    {
        if(chain[i]=='-')
            break
        else
        {
            if(k==0)
            {
                ret=chain[i]
            }
            else
            {
                ret=chain[i]+ret
            }
            k+=1
        }
        i--
    }
    return ret
}

passwords=input(2)

function AdventOfCode21()
{
    q=0
    valids=0
    while(q<passwords.length)
    {
        PassLine=passwords[q].split(' ')
        interval=PassLine[0]
        letter=PassLine[1]
        letter=letter[0]
        text=PassLine[2]

        if(letters(letter,text)>=ToDash(interval) & letters(letter,text)<=AfterDash(interval))
        {
            valids+=1
        }
        q+=1
    }
    return valids
}

function AdventOfCode22()
{
    q=0
    valids=0
    while(q<passwords.length)
    {
        PassLine=passwords[q].split(' ')
        interval=PassLine[0]
        letter=PassLine[1]
        letter=letter[0]
        text=PassLine[2]
        if(text[ToDash(interval)-1]==letter & text[AfterDash(interval)-1]!=letter)
        {
            valids+=1
        }
        else if(text[ToDash(interval)-1]!=letter & text[AfterDash(interval)-1]==letter)
        {
            valids+=1
        }
        q++
    }
    return valids
}
console.log(AdventOfCode21(), AdventOfCode22())
