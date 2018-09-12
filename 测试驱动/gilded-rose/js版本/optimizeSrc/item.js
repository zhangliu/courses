class Item {
    constructor(name, sellIn, quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }

    increaseQuality() {
        if (this.quality < 50) {
            this.quality = this.quality + 1;
        }
    }

    decreaseQuality() {
        if (this.quality > 0) {
            this.quality = this.quality - 1;
        }
    }
}