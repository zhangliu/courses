class ItemFactory {
    static create(itemName, sellIn, quality) {
        const itemClass = ItemFactory.map.get(itemName)
        return itemClass
            ? new itemClass(itemName, sellIn, quality)
            : new Item(itemName, sellIn, quality)
    }
}

ItemFactory.map = new Map([
    ['Sulfuras', SulfurasItem],
    ['AgedBrie', AgedBrieItem],
    ['Backstage', BackstageItem],
    ['Conjured', ConjuredItem],
    ['Normal', NormalItem]
])