from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt


class load_the_data:
    def __init__(self, url: str = None, path_tgz: str = None, csv_path: str = None):
        self.url = url
        self.path_tgz = path_tgz
        self.csv_path = csv_path

    def update_housing(self) -> pd.DataFrame:
        self.csv_path = "datasets/housing/housing.csv"
        self.url = "https://github.com/ageron/data/raw/main/housing.tgz"
        self.path_tgz = "datasets/housing.tgz"
        housing = self.load_data(
            url=self.url, path_tgz=self.csv_path, csv_path=self.csv_path
        )
        return housing

    def load_data(self, url: str, path_tgz: str, csv_path: str) -> pd.DataFrame:
        tarball_path = Path(path_tgz)
        if not tarball_path.is_file():
            Path("datasets").mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(url, tarball_path)
            with tarfile.open(tarball_path) as housing_tarball:
                housing_tarball.extractall(path="datasets")
        return pd.read_csv(Path(csv_path))

    def __str__(self):
        """
            this is just a means to check if we are inputting the correct

        Returns:
            str: This will return the 3 parameters that we need to run our function.
        """
        #
        # parameters.

        x = (
            f"The input parameters for this class are:"
            + f"\n url: {self.url} \n path_tgz: {self.path_tgz} \n "
            + f"csv_path: {self.csv_path}"
        )
        return x


if __name__ == "__main__":
    y = load_the_data()
    x = y.update_housing()
    end_line = "\n" + "-" * x.shape[1] + "\n"
    # print(x.head(), end=end_line
    print("We are now displaying the x.info() now on the line below", end=end_line)
    print(x.info(), end=end_line)
    print(
        "Below this we will be displaying the value_counts of x['ocean_proximity']",
        end=end_line,
    )
    print(x["ocean_proximity"].value_counts(), end=end_line)
    print(
        "Next we are describing the alues within x thoruhgh x.describe()", end=end_line
    )
    print(x.describe(), end=end_line)
    print(y.__str__())
    x.hist(bins=50, figsize=(12, 8))
    plt.show()
