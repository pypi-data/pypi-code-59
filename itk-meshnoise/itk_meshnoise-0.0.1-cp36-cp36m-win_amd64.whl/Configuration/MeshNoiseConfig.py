depends = ('ITKPyBase', 'ITKStatistics', 'ITKQuadEdgeMesh', 'ITKMesh', 'ITKCommon', )
templates = (
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMF2MF2', True, 'itk::Mesh<float,2>, itk::Mesh<float,2>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMF2DTF2MF2DTF2', True, 'itk::Mesh<float,2,itk::DefaultDynamicMeshTraits<float,2>>, itk::Mesh<float,2,itk::DefaultDynamicMeshTraits<float,2>>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMD2MD2', True, 'itk::Mesh<double,2>, itk::Mesh<double,2>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMD2DTD2MD2DTD2', True, 'itk::Mesh<double,2,itk::DefaultDynamicMeshTraits<double,2>>, itk::Mesh<double,2,itk::DefaultDynamicMeshTraits<double,2>>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMF3MF3', True, 'itk::Mesh<float,3>, itk::Mesh<float,3>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMF3DTF3MF3DTF3', True, 'itk::Mesh<float,3,itk::DefaultDynamicMeshTraits<float,3>>, itk::Mesh<float,3,itk::DefaultDynamicMeshTraits<float,3>>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMD3MD3', True, 'itk::Mesh<double,3>, itk::Mesh<double,3>'),
  ('AdditiveGaussianNoiseMeshFilter', 'itk::AdditiveGaussianNoiseMeshFilter', 'itkAdditiveGaussianNoiseMeshFilterMD3DTD3MD3DTD3', True, 'itk::Mesh<double,3,itk::DefaultDynamicMeshTraits<double,3>>, itk::Mesh<double,3,itk::DefaultDynamicMeshTraits<double,3>>'),
  ('Mesh', 'itk::Mesh', 'itkMeshF2DTF2', False, 'float,2,itk::DefaultDynamicMeshTraits<float,2>'),
  ('Mesh', 'itk::Mesh', 'itkMeshD2DTD2', False, 'double,2,itk::DefaultDynamicMeshTraits<double,2>'),
  ('Mesh', 'itk::Mesh', 'itkMeshF3DTF3', False, 'float,3,itk::DefaultDynamicMeshTraits<float,3>'),
  ('Mesh', 'itk::Mesh', 'itkMeshD3DTD3', False, 'double,3,itk::DefaultDynamicMeshTraits<double,3>'),
  ('PointSet', 'itk::PointSet', 'itkPointSetF2DTF2', False, 'float,2,itk::DefaultDynamicMeshTraits<float,2>'),
  ('PointSet', 'itk::PointSet', 'itkPointSetD2DTD2', False, 'double,2,itk::DefaultDynamicMeshTraits<double,2>'),
  ('PointSet', 'itk::PointSet', 'itkPointSetF3DTF3', False, 'float,3,itk::DefaultDynamicMeshTraits<float,3>'),
  ('PointSet', 'itk::PointSet', 'itkPointSetD3DTD3', False, 'double,3,itk::DefaultDynamicMeshTraits<double,3>'),
  ('AdditiveGaussianNoiseQuadEdgeMeshFilter', 'itk::AdditiveGaussianNoiseQuadEdgeMeshFilter', 'itkAdditiveGaussianNoiseQuadEdgeMeshFilterQEMD2QEMD2', True, 'itk::QuadEdgeMesh< double,2 >, itk::QuadEdgeMesh< double,2 >'),
  ('AdditiveGaussianNoiseQuadEdgeMeshFilter', 'itk::AdditiveGaussianNoiseQuadEdgeMeshFilter', 'itkAdditiveGaussianNoiseQuadEdgeMeshFilterQEMD3QEMD3', True, 'itk::QuadEdgeMesh< double,3 >, itk::QuadEdgeMesh< double,3 >'),
)
snake_case_functions = ('additive_gaussian_noise_quad_edge_mesh_filter', 'additive_gaussian_noise_mesh_filter', 'mesh_source', 'mesh_to_mesh_filter', )
