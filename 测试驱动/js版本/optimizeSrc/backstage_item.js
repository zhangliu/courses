class BackstageItem extends Item {
    handle() {
        this.sellIn = this.sellIn - 1;
        this.increaseQuality()
        if (this.sellIn < 10) {
            this.increaseQuality()
        }
        if (this.sellIn < 5) {
            this.increaseQuality()
        }
        if (this.sellIn < 0) {
            this.quality = 0;
        }
    }
}