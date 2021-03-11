# RL Benchmark
## Installation Guide
To configure a Python conda environment to run this project, follow these steps diligently:
1. Create a new conda environment  
```conda create --name rl-benchmark```
2. Activate that environment  
3. Install pip  
```conda install pip```
4. Install the correct version of Python  
```conda install python=3.6```
5. Install the FinRL package:  
```pip install git+https://github.com/AI4Finance-LLC/FinRL-Library.git```

## Description


## Tasks
1. Simulate stock based on Black-Scholes
2. Define reward as the value at horizon
3. See if optimal RL policy converges with optimal closed-form Merton problem solution

### Tasks: 21-01-21
1. Investigate how FinRL package ingests data
2. Based on how FinRL ingests data, create multiple sampling method to feed data into FinRL
3. Construct RL agent and visualize results


[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
