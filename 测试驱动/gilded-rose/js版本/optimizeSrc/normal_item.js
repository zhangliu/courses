class NormalItem extends Item {
    handle() {
        this.sellIn = this.sellIn - 1;
        this.decreaseQuality()
        if (this.sellIn < 0) {
            this.decreaseQuality()
        }
    }
}