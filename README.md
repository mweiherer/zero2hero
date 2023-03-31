# From Zero to Hero: Convincing with Extremely Complicated Math

### [Paper](https://eggerbernhard.ch/zero2hero.pdf) | [Code](https://github.com/mweiherer/zero2hero)

[Maximilian Weiherer](https://mweiherer.github.io/) and
[Bernhard Egger](https://eggerbernhard.ch/)<br>
Funky-Amusing-University (FAU) Erlangen-Nürnberg

This is the official implementation of the paper "From Zero to Hero: Convincing with Extremely Complicated Math", SIGBOVIK'23.

## Installation
We recommend to use [Anaconda](https://en.wikipedia.org/wiki/Anaconda) for dependency management. The following command creates an environment named 'zero2hero' on your local machine:
```
conda env create -f environment.yml
```
Activate the environment via `conda activate zero2hero`.

As stated multiple times in our paper, zero2hero uses a state-of-the-art, cutting-edge, next-generation large language model to turn notoriously simple math into insanely complex looking equations. In our case, it's ChatGPT. To enable command line access, we use the open-source [chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper). You already pip-installed this package with the above command; however, you still need to login into your OpenAI account. To do so, you can either follow the official documentation, or trust us and execute the following two steps (taken directly from the official documentation).

First, install a browser in playwright:
```
playwright install firefox
```

Second, start up the software in install mode:
```
chatgpt install
```

This opens up a browser window. Log in into ChatGPT with your OpenAI account (or sign up if you haven't sold your soul yet). Exit the program by typing `/exit` into the command line. That's it.

## Usage
Assuming a tex file 'your_file.tex' in the root directory, simply type
```
python zero2hero.py <your_file>
```
to make your paper being accepted at the top-tier conference you're dreaming of. Please make sure to submit 'your_file_complicate.tex'!

## Citation
In any case, please cite 

```
@inproceedings{weiherer2023zero2hero,
    author = {Weiherer, Maximilian and Egger, Bernhard},
    title = {From Zero to Hero: Convincing with Extremely Complicated Math},
    booktitle = {SIGBOVIK},
    year={2023}
}
```

Also, if our work helps you with your research, please consider adding us to the author list. In case you have any questions or suggestions for further improvements, please e-mail us. We may respond!

