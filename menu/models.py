from django.db import models


# class Menu(models.Model):
    # name = models.CharField(max_length=200)


class MenuNode(models.Model):
    name = models.CharField(max_length=200)
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"<MenuNode name={self.name}>"


# Closure table

class MenuNodeTree(models.Model):
    ancestor = models.ForeignKey(MenuNode, on_delete=models.CASCADE, related_name='ancestors')
    descendant = models.ForeignKey(MenuNode, on_delete=models.CASCADE, related_name='descendants')
    nearestAncestor = models.ForeignKey(MenuNode, on_delete=models.CASCADE, related_name='nearest_ancestors', null=True)
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    level = models.IntegerField()

    def __str__(self):
        return f"<MenuNodeTree ancestor={self.ancestor}, descendant={self.descendant}>"