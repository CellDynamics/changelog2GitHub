# changelog2GitHub
Convert `changes.xml` file from  [Apache Maven Changes Plugin](https://maven.apache.org/plugins/maven-changes-plugin/index.html) to plain Markdown formatted text.

## Example

Having `changes.xml` like that:

```xml
<document xmlns="http://maven.apache.org/changes/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/changes/1.0.0 http://maven.apache.org/xsd/changes-1.0.0.xsd">
  <properties>
    <title>QuimP Changelog</title>
    <author email="p.baniukiewicz@warwick.ac.uk">Piotr Baniukiewicz</author>
  </properties>
  <body>
    <release date="2017-12-10" description="Release" version="17.12.02">
      <action dev="baniuk" issue="271" type="fix">QuimP-BOA: Fixed wrong frames reported in BOA status log on error.
         </action>
      <action dev="baniuk" issue="274" type="add">QuimP-BOA: Added Freeze Cell button. Frozen cells are not modified when segmentation options are changed.
         </action>
      <action dev="baniuk" issue="278" type="update">QuimP-RandomWalk: Increased number of fractional digits in some controls in plugins.
         </action>
      <action dev="baniuk" issue="" type="update">QuimP-API: Added new types of controls in QWindowBuilder.
         </action>
      <action dev="baniuk" issue="" type="fix">QuimP-BOA: Fixed possible exception when Add Cell button was used without ROI. Also fixed empty error window when wrong file was loaded.
         </action>
      <action dev="baniuk" issue="" type="update">QuimP-RandomWalk: Changed UI to horizontal.
         </action>
    </release>
    <release date="2017-12-08" description="Internal Release" version="17.12.01">
      <action dev="baniuk" issue="275" type="update">QuimP-RandomWalk: Allow to set relative error in Random Walk plugin. This solves problem with ending iterative process too early. There is also new option for better estimation of background level in automatic seed propagation mode.
         </action>
      <action dev="baniuk" issue="274" type="add">QuimP-BOA: New setting that allows to process only cell that is currently zoomed in. Other cells are frozen and they are not touched when either segmentation options or filters are changed.  
         </action>
    </release>
  </body>
</document>
 ```
 And then calling:
 ```bash
 python changelog2GitHub/changelog2GitHub.py src/changes/changes.xml
```

One gets:

This release fixes:
 * __[B]__ #271 QuimP-BOA: Fixed wrong frames reported in BOA status log on error.
 * __[F]__ #274 QuimP-BOA: Added Freeze Cell button. Frozen cells are not modified when segmentation options are changed.
 * __[U]__ #278 QuimP-RandomWalk: Increased number of fractional digits in some controls in plugins.
 * __[U]__ # QuimP-API: Added new types of controls in QWindowBuilder.
 * __[B]__ # QuimP-BOA: Fixed possible exception when Add Cell button was used without ROI. Also fixed empty error window when wrong file was loaded.
 * __[U]__ # QuimP-RandomWalk: Changed UI to horizontal.
 
_Legend: [B] - bugfix, [F] - feature added, [U] - update or enhancement_
