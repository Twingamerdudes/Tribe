# How to contribute
You can contribute in many ways, you can suggest new ideas, submit pull requests, or reporting bugs.
This file will tell you how to do that.
# Bugs
All bugs should be reported in the Issuses tab. The bug should meet these requirements
* Describe the bug
* What is the excepted behavior

Here is what you should include but are not required:
* Solutions you have tired
* Error logs
* Screenshots
* Code

Here is a template that you can use:

Bug:
Humans do nothing when I make a simulation.

Excepted Behavior:
Humans move around to try and find food and water.

Code:
```python
while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    for tribe in simulation.tribeList:
      tribe.update()
    for house in simulation.houseList:
      house.update()
    screen.fill((0, 0, 0))
    for food in simulation.foodList:
      food.draw(screen)
    for water in simulation.waterList:
      water.draw(screen)
    for wood in simulation.woodList:
      wood.draw(screen)
    for house in simulation.houseList:
      house.draw(screen)
    for human in simulation.humanList:
      human.draw(screen)
```
# Submitting pull requests
You want to add on or fix bugs of Tribe, amazing, here's how should do it.

Here are the requirements to get you're code to be submitted
* Should have some comments in major changes.
* Should follow variable naming conventions (consts should be uppercase and have underscores as spaces, other variables should use camel case)
* Should change the code in some way (Fixs a bug, or adds a new features)

Here are some stuff you should do but don't have to:
* Make you're code backwards compatiable.
* Code should try to be modular. If you add a new feature but it doesn't fit with the other files, create a new one.

If you follow these guidelines you're pull request will likly be accpeted. This does not mean it will be accpeted, just will have a higher chance of being
accpeted.

# Recommending Ideas
All idea's should be in the issues tab (GitHub should really rename that tab). If you're idea seems like it would be a good fit for the library, it will probably
be added. You're idea should also follow these requirements:
* The idea can't be something that is already in tribe. (ex. You recommend humans -_-)
* The idea should be reasonable, don't ask for a programming language built ontop of this.

Things you should do but are not required:
* Describe you're idea in more detail, you don't want a result that doesn't satisfy you.
* Provide examples of you're idea, again, you don't want a result that doesn't satisfy you.

Now that you know how to contribute, what are you waiting for! We are ready to see what you bring to the table.
