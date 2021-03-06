# pyDESDEO #

The pyDESDEO is free and open source framework for developing and
experimenting with interactive multiobjective optimization. 

## Introduction ##

There exist many methods to solve [multiobjective optimization](https://en.wikipedia.org/wiki/Multi-objective_optimization) problems. Methods which introduce some preference information into the solution process are commonly known as multiple criteria decision making methods. When using so called [interactive methods](https://en.wikipedia.org/wiki/Multi-objective_optimization#Interactive_methods), the decision maker (DM) takes an active part in an iterative solution process by expressing  preference information at several iterations. According to the given preferences, the solution process is updated at each iteration and one or several new solutions are generated. This iterative process continues until the DM is sufficiently satisfied with one of the solutions found. 

Many interactive methods have been proposed and they differ from each other e.g. in the way 
preferences are expressed and how the preferences are utilized when new solutions. The aim of the DESDEO is to implement aspects common for different interactive methods, as well as provide framework for developing and implementing new methods. 

## Architecture ##

Overview of the current DESDEO architecture is shown in diagram

![DESDEO Overview](https://github.com/industrial-optimization-group/pyDESDEO/raw/master/doc/design/overview.png)

# Interactive Methods  #

## NAUTILUS Method ##

Most interactive methods developed for solving multiobjective optimization problems sequentially generate Pareto optimal solutions and the  decision maker must always trade-off to get a new solution. Instead, the family of interactive trade-off-free  methods called NAUTILUS starts from the worst possible objective values and improves every objective function step by step according  to the preferences of the decision maker. Recently, the NAUTILUS family has been presented as a general NAUTILUS framework consisting of several modules.  To extend the applicability of interactive methods, it is recommended that a reliable software implementation,  which can be easily connected to different simulators or modelling tools, is publicly available. In this paper, we bridge the gap between presenting an algorithm and implementing it and propose a general software framework for the NAUTILUS family which facilitates the implementation of all the NAUTILUS methods, and even other interactive methods. This software framework has been designed following an object-oriented architecture and consists of several software blocks designed to cover independently the different requirements of the NAUTILUS framework. To enhance wide applicability, the implementation is available as open source code. The functioning and flexibility of the NAUTILUS software framework is demonstrated with two numerical example problems.
