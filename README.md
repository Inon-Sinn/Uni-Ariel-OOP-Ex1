This project was created by Inon.S, Yaron.S

# Uni-Ariel-OOP-Ex1

In this Assignment we had to write an offline Elevator Algorithem which gives the user the best way to distribute the elevators given a list of calls.
What is a call? A call is the data of person who called for the elevator, we get the time at which he called the elevator, his positon, destination and the id of Elevator it is allocated to, by default -1 (not a existing elevator).

Our input is a json which represented a Building and a csv which represented a list of calls. And the output is a csv of the calls with a possible allocation (not -1 for every caller)

# The Objects we made

**CallForElevator:** Represents a call<br />
**Elevator:** Represents a Elevator<br />
**Building:** Represents the Building in which we got the calls<br />
**BLock:** Just a block of data we use in the algorithem which makes our lives easier<br />
**Allocation:** This Class is Responsible to allocate the calls <br />

![alt text](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex1/blob/master/Clases_PUML.png)

# The Algorithem 

Our algorithem is a Greedy algorithem.<br/>
**In what way is it Greedy?** Total time - the total amount of time all calls took to finish<br/>
**How is it Implemented?** The CLass Allocation, for ever call it allocates it creates a kind of simulation. For every Elevator the building has it takes it's list of calls allocated to it and then adds the new call. after which it calcualtes by how much the Total time has grown with the added call. it will then allocate the call to elevator with the minimum growth in Total time.

  <li> We Collect the Building json and the Call list Csv in the main and translate it to the objects we created so we can work with it (<em>Building</em>,<em>CallForElevator</em>)</li>
  <li>Create a new <em>Allocation</em>(see above) with the Building and the Call list, which will in its initation already allocate the calls to the Elevators in the Building</li>
    <ol>
      <li>Create for every Elevator a list which will represent its work flow from the start to the end with a list of Blocks, it will be sorted by time.<br/>
        A BLock will represent every moment of change or event possible in the work flow: The time we got the call, the moment we got to the callers positon or destination, the moment we finish collecting or dropping of the caller and the moment the Elvator changes direction </li>
      <li>Go over the Calls and allocate each with the function <em>allocate_call</em></li>
      <li><em>allocate_call</em>: Make a copy of each Elevator work flow list <em>total_list[Elevator.id]</em> and then add the given call to it with <em>add</em></li>
      <li> <em>add</em>: call the function <em>add_call_time</em> which adds a block, that represents the moment we got the call, to the work flow, by time</li>
      <li> <em>add</em>: call the functions <em>add_stop</em> which adds blocks that represent stopping and collecting the caller from its position <em>CallForElevator.src</em>, they will be added behind the block of call_time, by place </li>
      <li><em>add</em>: call the functions <add_stop> which adds blocks that represent stopping and dropping the caller in its destination <em>CallForElevator.dest</em>, they will be added behind the block of the callers position <em>CallForElevator.src</em>, by place.<br/> finished <em>add</em> </li>
      <li>use <em>add</em> on the real work flow list of the elevators with the least amount of growth of total time </li>
    </ol>
  </li>
  <li>With <em>Allocation</em> and the Call list create a new Call list with the allocations and then translate it back to a Csv which will be our output
</li>
</ol> 
        
<h2>After Word</h1>
        This was a fun project and the results aren't bad, the only thing i would do is if i have time to come back to this project is find the bug that made the algorithem worse by somehow allocating the same elevator for a bunch of calls we got at almost the same time. And maybe finding way to make it even more efficent.
