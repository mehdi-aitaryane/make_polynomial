# make_polynomial

The `make_polynomial` function in the `datasets.py` module generates a dataset of points that follow a polynomial function. It allows for the creation of samples with different features, degree, noise, and random state.

## Mathematics Behind the Algorithm

The make_polynomial function uses the concept of power functions to generate points that follow a polynomial function.
The make_polynomial function generates the input data X by sampling random values from a uniform distribution over a specified range. It then adds Gaussian noise to the input data to introduce some variation. It generates the output data y by applying a polynomial function to the sum of all features in X. The degree and the coefficients of the polynomial function are determined by the parameters of the function.

## Pseudocode of the Algorithm

```
Procedure make_polynomial

Initialize the number of samples, features, degree, noise, and random state.

1. Generate the input data X by sampling random values from a uniform 

2. distribution over a specified range.

3. Add noise to the input data by adding random values from a normal 

4. distribution with a specified scale.

5. Generate the output data y by applying a polynomial function to the sum of all features in X.

6. Return the input data X and the output data y.
```

## Modules

The project contains two modules:

datasets.py: Contains the make_polynomial function for generating the dataset.
plots.py: Contains the plot2D and plot3D functions for visualizing the dataset.

## Notebook

A Jupyter notebook demonstrating the usage of the make_polynomial function and the visualization functions is included in the repository.

## Usage

To use the make_polynomial function, import it from the datasets module and call it with the desired parameters. The function returns an input data X and an output data y, which can be visualized using the plot2D or plot3D functions from the plots module.

## Contributing
Contributions to the project are welcome. Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
